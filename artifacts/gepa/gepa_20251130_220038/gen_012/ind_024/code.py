
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A (7th)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # B (9th)
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5),  # C (chromatic)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # C# (11th)
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # D (root)
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),  # F (3rd)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G7
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=start + 3.0)
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (67), A (71), B (71) — sing, leave it, return
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.75),  # B
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dantes_intro.mid")
