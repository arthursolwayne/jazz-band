
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm7 (F, Ab, Bb, D) - motif starts on F, moves up to Ab, then to Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0), # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm, chromatic approach to F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0), # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.5), # F
]
bass.notes.extend(bass_notes)

# Piano: F7 chord (F, Ab, Bb, C) on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=95, pitch=68, start=1.75, end=2.0), # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=1.75, end=2.0), # C
    pretty_midi.Note(velocity=95, pitch=71, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=95, pitch=68, start=2.75, end=3.0), # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=2.75, end=3.0), # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=2.75, end=3.0), # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but descend
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5625), # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approach to Ab
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=90, pitch=45, start=3.25, end=3.5), # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=3.5, end=3.75), # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.0), # F
]
bass.notes.extend(bass_notes)

# Piano: F7 chord on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=95, pitch=68, start=3.25, end=3.5), # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=3.25, end=3.5), # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=3.25, end=3.5), # C
    pretty_midi.Note(velocity=95, pitch=71, start=4.25, end=4.5), # F
    pretty_midi.Note(velocity=95, pitch=68, start=4.25, end=4.5), # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=4.25, end=4.5), # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=4.25, end=4.5), # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif again, this time ascending, finishing on Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0), # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0), # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=90, pitch=45, start=5.5, end=5.75), # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=5.75, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Piano: F7 chord on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=95, pitch=68, start=4.75, end=5.0), # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=4.75, end=5.0), # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=4.75, end=5.0), # C
    pretty_midi.Note(velocity=95, pitch=71, start=5.75, end=6.0), # F
    pretty_midi.Note(velocity=95, pitch=68, start=5.75, end=6.0), # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=5.75, end=6.0), # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=5.75, end=6.0), # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
