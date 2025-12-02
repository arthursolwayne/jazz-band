
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif - D, F#, B, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line in D minor (D, Eb, F, G)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: D7 chord on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # C
]
# Bar 3: G7 chord on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # F
])
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif but with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line in D minor (D, Eb, F, G) again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3: G7 chord on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # F
]
# Bar 4: D7 chord on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # C
])
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line in D minor (D, Eb, F, G) again
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # G
]
bass.notes.extend(bass_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=38, start=3.0, end=3.375),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=38, start=4.5, end=4.875),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=95, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=38, start=6.0, end=6.375),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
