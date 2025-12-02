
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comps on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0)
drums.notes.extend(drum_notes)

# Saxophone: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # E (Dm7 - E is the 9th)
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # D (root)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F (7th)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # E (9th)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # D (root)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # E (9th)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F (7th)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # E (9th)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
