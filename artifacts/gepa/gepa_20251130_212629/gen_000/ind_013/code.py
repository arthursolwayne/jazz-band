
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875)  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # F (69)
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0), # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # D
]
piano.notes.extend(piano_notes)

# Sax: Motif again, with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5), # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # D#
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0), # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # D
]
piano.notes.extend(piano_notes)

# Sax: Motif again, with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0), # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875)  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.1875)  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
