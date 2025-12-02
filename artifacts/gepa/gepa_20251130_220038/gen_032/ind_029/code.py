
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    # D (2nd fret, 5th string) = 62
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    # Eb (3rd fret, 5th string) = 63
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),
    # F# (5th fret, 5th string) = 65
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),
    # G (6th fret, 5th string) = 67
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=2.25),
    # D7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=74, start=2.625, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: Melody in D
# Motif: D (62) - E (64) - F# (65) - G (67), then repeat but end on F#
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Bass continues
bass_notes = [
    # D (2nd fret, 5th string) = 62
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    # Eb (3rd fret, 5th string) = 63
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75),
    # F# (5th fret, 5th string) = 65
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),
    # G (6th fret, 5th string) = 67
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=74, start=3.375, end=3.75),
    # D7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues, motif repeated but ends on F#
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Bass continues
bass_notes = [
    # D (2nd fret, 5th string) = 62
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    # Eb (3rd fret, 5th string) = 63
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25),
    # F# (5th fret, 5th string) = 65
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),
    # G (6th fret, 5th string) = 67
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Bar 4: Piano continues
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=74, start=4.875, end=5.25),
    # D7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=6.0, end=6.375),
    pretty_midi.Note(velocity=95, pitch=67, start=6.0, end=6.375),
    pretty_midi.Note(velocity=95, pitch=71, start=6.0, end=6.375),
    pretty_midi.Note(velocity=95, pitch=74, start=6.0, end=6.375)
]
piano.notes.extend(piano_notes)

# Bar 4: Sax continues, ends with a rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
