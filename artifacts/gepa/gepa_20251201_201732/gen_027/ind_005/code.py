
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drums_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (2), F# (3), G (4), A (5)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),
    # Bar 3: C# (2), D (3), F# (4), G (5)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
    # Bar 4: A (2), B (3), C# (4), D (5)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: D (62), F# (67), D (62) - start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125),
    # Bar 3: G (67), Bb (69), A (69) - leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),
    # Bar 4: D (62), C# (60), D (62) - finish the motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.125),
]
for note in sax_notes:
    sax.notes.append(note)

# Add drums for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start_time = (bar - 1) * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.25)
    # Hihat
    for i in range(4):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.375)

# Add to MIDI
drums.notes.extend([pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.375) for t in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
