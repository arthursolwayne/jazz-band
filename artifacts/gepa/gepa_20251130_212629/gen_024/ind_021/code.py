
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
    # Kick on 1 and 3 (0.0, 0.75, 1.5)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.1),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.85),
    # Snare on 2 and 4 (0.375, 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=0.375, end=0.475),
    pretty_midi.Note(velocity=110, pitch=38, start=1.125, end=1.225),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.225),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.35),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.475),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.6),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.725),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.85),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=0.975),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.1),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.225),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.35),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.475),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6),   # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.6, end=1.7),   # C
    pretty_midi.Note(velocity=90, pitch=63, start=1.7, end=1.8),   # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=1.8, end=1.9),   # E
    pretty_midi.Note(velocity=90, pitch=66, start=1.9, end=2.0),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.1),   # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.1, end=2.2),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.2, end=2.3),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.3, end=2.4),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.4, end=2.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.6),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.6, end=2.7),   # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.7, end=2.8),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.8, end=2.9),   # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.9, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.1),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.1, end=3.2),   # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.2, end=3.3),   # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=3.3, end=3.4),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.4, end=3.5),   # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.6),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.6, end=3.7),   # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.7, end=3.8),   # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.8, end=3.9),   # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.9, end=4.0),   # D
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.6),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.6),   # B
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.6),   # A
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.6),   # E
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.1),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.1),   # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.1),   # A
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.1),   # E
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.6),   # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=2.6),   # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.6),   # A
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.6),   # E
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.6, end=1.7),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.7, end=1.8),   # G
    pretty_midi.Note(velocity=100, pitch=66, start=1.8, end=1.9),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.1),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.1, end=2.2),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.2, end=2.3),   # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.3, end=2.4),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.6),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.6, end=2.7),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.7, end=2.8),   # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.8, end=2.9),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.1, end=3.2),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.2, end=3.3),   # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.3, end=3.4),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
