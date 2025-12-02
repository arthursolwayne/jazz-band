
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

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass: Walking line in Fm
# Fm: F, Ab, D, C
# Chromatic approaches: E#, Gb, Eb, Db

# Bar 2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F (Ab)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Ab7 on 4

# Bar 2: Fm7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
]

# Bar 2: Ab7 on beat 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.5),  # G
])

piano.notes.extend(piano_notes)

# Sax: Motif 1 (F, Ab, G, Eb) - start on beat 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm
# Fm: F, Ab, D, C
# Chromatic approaches: E#, Gb, Eb, Db

# Bar 3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F (Ab)
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Ab7 on 4

# Bar 3: Fm7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # D
]

# Bar 3: Ab7 on beat 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.0),  # G
])

piano.notes.extend(piano_notes)

# Sax: Motif 2 - continuation of the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Fm
# Fm: F, Ab, D, C
# Chromatic approaches: E#, Gb, Eb, Db

# Bar 4
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F (Ab)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Ab7 on 4

# Bar 4: Fm7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # D
]

# Bar 4: Ab7 on beat 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.5),  # G
])

piano.notes.extend(piano_notes)

# Sax: Motif 3 - resolution of the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # Ab
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
