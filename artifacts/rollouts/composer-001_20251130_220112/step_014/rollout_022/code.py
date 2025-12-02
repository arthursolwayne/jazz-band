
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625), # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75), # Hihat &
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),  # Hihat &
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # Fm7 - F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Ab - G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # Bb - A
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # F - F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # Ab - G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # Bb - A
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=34, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=2.75, end=3.0),  # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=36, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=2.0),  # D
    # Bar 2, beat 4: Fm7
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.75, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=34, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=34, start=4.25, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=36, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.25, end=3.5),  # D
    # Bar 3, beat 4: Fm7
    pretty_midi.Note(velocity=100, pitch=36, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.25, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=34, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=5.5, end=5.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Fm7
    pretty_midi.Note(velocity=100, pitch=36, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0),  # D
    # Bar 4, beat 4: Fm7
    pretty_midi.Note(velocity=100, pitch=36, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=43, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=5.75, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625), # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.25), # Hihat &
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375), # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.625), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125), # Hihat 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.8125, end=3.0),  # Hihat &
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625), # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75), # Hihat &
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375), # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125), # Hihat 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),  # Hihat &
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625), # Hihat 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25), # Hihat &
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375), # Hihat 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625), # Hihat &
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125), # Hihat 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0),  # Hihat &
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
