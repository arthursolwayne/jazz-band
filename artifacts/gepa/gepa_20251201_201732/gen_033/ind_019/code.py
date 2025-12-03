
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bass line (F2 - C3, MIDI 53 - 60)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G (Fmaj7 3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # B (Fmaj7 7th)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line (F2 - C3, MIDI 53 - 60)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: F#m7 (F#, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.5),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.5),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # A (F#m7 3rd)
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # C (F#m7 5th)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line (F2 - C3, MIDI 53 - 60)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # B (F7 7th)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # C (F7 5th)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
