
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Bb (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # Eb (chromatic down)
    pretty_midi.Note(velocity=90, pitch=37, start=2.625, end=3.0),  # Ab (chromatic down)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif (F, Ab, Bb, F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125), # G (chromatic up)
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),  # Gb (chromatic down)
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Motif variation (Bb, F, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.625), # G (chromatic up)
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # Gb (chromatic down)
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=68, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif variation (F, Ab, Bb, F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and Bar 4
# Bar 3: Kick on 1, Snare on 2, Kick on 3, Snare on 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
# Bar 4: Kick on 1, Snare on 2, Kick on 3, Snare on 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Add hihat on every eighth
for i in range(0, 6, 0.375):
    pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
