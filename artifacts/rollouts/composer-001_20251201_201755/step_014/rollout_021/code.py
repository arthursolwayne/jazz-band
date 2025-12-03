
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # G2
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # F#2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.625),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),   # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),   # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),   # C#4
]
# Bar 3: Gmaj7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),   # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=3.0),   # D4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),   # F#4
])
# Bar 4: C#m7 (C#, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # C#4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.75),   # E4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),   # G4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.75),   # B4
])
for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25), # B4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75), # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25), # B4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # G4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Full in bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25))

    # Hihat on every eighth
    for t in [bar_start + 0.0, bar_start + 0.375, bar_start + 0.75, bar_start + 1.125,
              bar_start + 1.5, bar_start + 1.875, bar_start + 2.25, bar_start + 2.625]:
        if t < bar_start + 3.0:
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
