
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375))  # snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))  # snare on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # hihat on every eighth

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - walking bass line (D7 chord: D F# A C#)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)) # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25))# Eb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625))# E
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)) # F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375)) # G
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75)) # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125)) # A
bass.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5))  # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875))  # B
bass.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25)) # C#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625)) # D
bass.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0))  # E

# Diane - comping on 2 and 4 with 7th chords
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25)) # D7: D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)) # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25)) # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25)) # C#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875))  # D7 on 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875))

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)) # kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875)) # kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)) # snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5)) # snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25)) # kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)) # snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=6.0))    # hihat on every eighth

# Dante - sax solo (motif, start on bar 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25)) # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)) # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))  # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)) # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125)) # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5))  # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875))  # E
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25)) # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625)) # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0))  # E

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
