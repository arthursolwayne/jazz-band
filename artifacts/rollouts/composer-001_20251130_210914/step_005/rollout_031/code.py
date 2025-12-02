
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS LINE - Marcus (walking line, chromatic approaches, no repeated notes)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# PIANO - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # E7 (F7)
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # B7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # E7
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # E7 (F7)
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),  # B7
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # E7
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # E7 (F7)
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # B7
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # E7
]
piano.notes.extend(piano_notes)

# DRUMS - Bar 2-4 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    bar_start = 1.5 * (bar - 1)
    # 1
    pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.0, end=bar_start + 0.375)
    # 2
    pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    # 3
    pretty_midi.Note(velocity=90, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
    # 4
    pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 2.25, end=bar_start + 2.625)
drums.notes.extend(drum_notes)

# SAX - You (melody in F, one short motif, start, leave it hanging, come back and finish it)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F (return)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
