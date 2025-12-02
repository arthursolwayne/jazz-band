
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

kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # D
]
piano.notes.extend(piano_notes)

# Sax: Motif - start with a short phrase that sings, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5), # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # D
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, but don't resolve yet
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D7
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # D
]
piano.notes.extend(piano_notes)

# Sax: Resolve the motif with a final note that lingers
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
