
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

# Bar 2: Everyone in (1.5 - 3.0s)

# Bass line - walking line, chromatic approaches
bass_notes = [
    # Root on downbeats, chromatic passing tones on upbeats
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, sparse comp
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625), # C
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0), # F#
    pretty_midi.Note(velocity=85, pitch=76, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0), # C
]
piano.notes.extend(piano_notes)

# Sax - sparse motif, starts on beat 2, ends on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5), # G
    pretty_midi.Note(velocity=115, pitch=67, start=2.625, end=2.875), # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25), # F
]
sax.notes.extend(sax_notes)

# Bar 3: Continue the story (3.0 - 4.5s)

# Drums
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

# Bass line - walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=66, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, sparse comp
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125), # C
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=85, pitch=76, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875), # C
]
piano.notes.extend(piano_notes)

# Sax - continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25), # B
    pretty_midi.Note(velocity=115, pitch=67, start=3.375, end=3.625), # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=120, pitch=69, start=4.125, end=4.375), # B
    pretty_midi.Note(velocity=115, pitch=67, start=4.375, end=4.625), # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.875), # F
]
sax.notes.extend(sax_notes)

# Bar 4: Final bar (4.5 - 6.0s)

# Drums
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

# Bass line - walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, sparse comp
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=85, pitch=76, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625), # C
    # D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=72, start=6.0, end=6.375), # D
    pretty_midi.Note(velocity=80, pitch=74, start=6.0, end=6.375), # F#
    pretty_midi.Note(velocity=85, pitch=76, start=6.0, end=6.375), # A
    pretty_midi.Note(velocity=90, pitch=79, start=6.0, end=6.375), # C
]
piano.notes.extend(piano_notes)

# Sax - finish the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=115, pitch=69, start=4.875, end=5.125), # B
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5), # A
    pretty_midi.Note(velocity=120, pitch=64, start=5.625, end=5.875), # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
