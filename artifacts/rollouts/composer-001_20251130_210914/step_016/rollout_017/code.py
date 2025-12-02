
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-Hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
# D minor key, 160 BPM, 4/4 time
# Bar 2: Dm7 -> G7 -> Cmaj7 -> F7 -> Bm7 -> E7 -> Am7 -> D7
# Bass line: D - C# - C - B - A - G - F# - F - E - D - C - B - A - G - F - E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),   # C#
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.5),   # B
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75),   # A
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),   # F#
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),   # E
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=80, pitch=47, start=4.25, end=4.5),   # B
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=80, pitch=41, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.5),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4 (in bars 2-4)
# Dm7, G7, Cmaj7, F7, Bm7, E7, Am7, D7
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),   # G
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),   # B
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),   # F
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=80, pitch=74, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.25),   # F
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),   # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),   # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=2.75),   # B
    # Bar 5 (3.0 - 3.5s)
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),   # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),   # E
    # Bar 6 (3.5 - 4.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),   # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75),   # F
    # Bar 7 (4.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=57, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),   # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),   # G
    # Bar 8 (4.5 - 5.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),   # B
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75),   # F
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 -> G7 -> Cmaj7 -> F7
# Motif: D - F - G - B (Dm7)
# Repeat: G - B - D - F (G7)
# End: C - E - G - B (Cmaj7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6, end=1.7),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.7, end=1.8),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.8, end=1.9),   # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.9, end=2.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.1),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.1, end=2.2),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.2, end=2.3),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.3, end=2.4),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.4, end=2.5),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.6),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.6, end=2.7),   # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.7, end=2.8),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.8, end=2.9),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.9, end=3.0),   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
