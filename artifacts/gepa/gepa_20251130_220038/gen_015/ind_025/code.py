
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D

    # Bar 3: Dm7 -> F7
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5), # F

    # Bar 4: F7 -> Dm7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C

    # Bar 2: F7 on beat 3
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875), # E
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.875), # G

    # Bar 3: F7 on beat 1
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25), # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25), # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25), # G

    # Bar 3: Dm7 on beat 3
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.375), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.375), # C

    # Bar 4: Dm7 on beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75), # C

    # Bar 4: F7 on beat 3
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.875), # E
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.875), # G
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm, sing it, leave it hanging
sax_notes = [
    # Bar 2: Motif start (D, Eb, F, Gb)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0), # Gb

    # Bar 3: Repeat motif
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5), # Gb

    # Bar 4: Finish the motif with a resolution
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # A
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    for beat in [0, 2]:
        start = 1.5 + (bar * 1.5) + (beat * 0.75)
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2 and 4
    for beat in [1, 3]:
        start = 1.5 + (bar * 1.5) + (beat * 0.75)
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
    # Hi-hat on every eighth
    for eighth in range(4):
        start = 1.5 + (bar * 1.5) + (eighth * 0.375)
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
