
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.125), # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.125, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375), # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.5), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=2.875), # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0), # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0), # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.0), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0), # Eb
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=2.75), # A
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=2.75), # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75), # C
    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5), # G#
    pretty_midi.Note(velocity=100, pitch=75, start=3.375, end=3.5), # G
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.5), # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.5), # Bb
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Sax: Bar 2-4 (1.5 - 6.0s)
# Motif: F - Bb - G - Eb
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0), # Eb
    # Leave it hanging for a bar, then come back
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.125, end=3.25), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5), # Eb
    # Repeat the motif with a slight variation
    pretty_midi.Note(velocity=110, pitch=70, start=3.5, end=3.625), # F
    pretty_midi.Note(velocity=110, pitch=74, start=3.625, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.0), # Eb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.125, end=3.25), # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625), # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.625, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875), # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=3.875, end=4.0), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.375), # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=4.375, end=4.5), # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.5), # Bb
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.5), # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5), # C
    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.25), # G#
    pretty_midi.Note(velocity=100, pitch=75, start=4.125, end=4.25), # G
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.25), # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.25), # Bb
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.625), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.0), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.125), # G
    pretty_midi.Note(velocity=90, pitch=70, start=5.125, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375), # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=5.375, end=5.5), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=5.75), # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=5.875), # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=5.875, end=6.0), # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.0), # G#
    pretty_midi.Note(velocity=100, pitch=75, start=4.875, end=5.0), # G
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.0), # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.0), # Bb
    # Bar 4: End with a F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.75), # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=5.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=5.75), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75), # Eb
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
