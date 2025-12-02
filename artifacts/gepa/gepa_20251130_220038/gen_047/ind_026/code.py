
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hi-hat on &1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hi-hat on &2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hi-hat on &3
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hi-hat on &4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),   # F7: F, A, C, E♭
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F7 again on 4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
]
piano.notes.extend(piano_notes)

# Sax: motif, start on Bb, then G, then Bb again — short and haunting
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=2.625, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # B#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),   # G7: G, B, D, F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # G7 again on 4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Sax: motif continuation, more tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hi-hat on &1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hi-hat on &2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hi-hat on &3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hi-hat on &4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # B7: B, D#, F#, A
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # B7 again on 4
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax: motif resolution, ascending tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25),   # B
    pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=110, pitch=77, start=5.5, end=6.0),    # C (held)
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
