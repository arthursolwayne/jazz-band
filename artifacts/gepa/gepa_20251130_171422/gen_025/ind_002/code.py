
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add dynamic variation and space
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=70, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=70, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Saxophone motif - concise, emotional, with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Dm7 (D)
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # F (upper neighbor)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Eb
]

# Bass line - chromatic approaches, active and melodic
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C (chromatic)
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=49, start=5.625, end=6.0),  # C
]

# Piano comping - 7th chords, 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=70, pitch=67, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=70, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=69, start=1.5, end=1.875),  # Dm7 (D, F, Ab, C)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=70, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=70, pitch=69, start=2.25, end=2.625), # Dm7
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=70, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=70, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=70, pitch=69, start=3.0, end=3.375),  # Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=70, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.875),  # Dm7
]

drums.notes.extend(drum_notes)
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
