
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375))  # F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75))  # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=39, start=4.5, end=4.875))  # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625))  # F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0))  # G

# PIANO: 7th chords on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875))  # F7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875))

# DRUMS: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0))

# Bar 3 (3.0 - 4.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5))

# Bar 4 (4.5 - 6.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0))

# SAX: Tenor motif - F, Ab, Bb, D, F (Fm scale, syncopated)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0))  # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.125))  # F

# Repeat motif with variation
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.625))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.875, end=4.0))  # Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.375))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.125))  # F

# Final resolution
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.625))  # F

midi.instruments.extend([sax, bass, piano, drums])

midi.save('fm_intro.mid')
