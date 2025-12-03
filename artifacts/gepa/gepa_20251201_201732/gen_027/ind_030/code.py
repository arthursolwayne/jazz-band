
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> F#2 (41) -> G2 (43) -> A2 (45)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),

    # Bar 3: A2 (45) -> B2 (47) -> C#3 (49) -> D3 (50)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),

    # Bar 4: D3 (50) -> F#3 (53) -> G3 (55) -> A3 (57)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C#4
]
# Bar 3: F#7 (F#-A#-C#-E)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.5),  # A#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # C#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # E4
])
# Bar 4: G7 (G-B-D-F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # F#4
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F#4, Bb4, D5 — but leave it hanging at Bb4, resolve with D5 at the end of bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),     # D5 (resolve)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    for bar_start in [1.5, 3.0]:
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
        # Snare on 2 and 4
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
        # Hihat on every eighth
        for eighth in [0, 0.375, 0.75, 1.125, 1.5, 1.875]:
            pretty_midi.Note(velocity=100, pitch=42, start=bar_start + eighth, end=bar_start + eighth + 0.1875)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
