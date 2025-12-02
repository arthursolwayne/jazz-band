
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
# Sax: Start of motif
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)
sax.notes.append(sax_note)

# Bass: Walking line (F, Gb, G, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),  # C
    # Bar 2, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),   # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_note = pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375)
sax.notes.append(sax_note)

# Bass: Walking line (Bb, B, C, D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75),  # C
    # Bar 3, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),   # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish motif
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)
sax.notes.append(sax_note)

# Bass: Walking line (Eb, F, F#, G)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # C
    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),   # C
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
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

# Save the MIDI file
midi.write("dante_intro.mid")
