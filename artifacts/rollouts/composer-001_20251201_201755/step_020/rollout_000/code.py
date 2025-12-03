
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (bar 2, beat 1)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # G2 (bar 2, beat 2)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 (bar 2, beat 3)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 (bar 2, beat 4)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2 (bar 3, beat 1)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # G2 (bar 3, beat 2)
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2 (bar 3, beat 3)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 (bar 3, beat 4)
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # C2 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F5
])

# Bar 4: D9 (D F# A C E)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # E5
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F#4 (67) -> A4 (71) -> D5 (72) -> A4 (71) -> D4 (62) (start on beat 1 of bar 2, end on beat 2 of bar 3)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0),  # D5
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.125),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.25),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D4 (reprise)
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.5),  # D5
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.625),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=4.875),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.0),  # D5
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.125),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25))
    # Hihat on every eighth
    for i in range(0, 4):
        hihat_start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
