
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5, cutoff=0.25)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS LINE (Marcus)
# Walking line in F, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=78, start=5.625, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# PIANO (Diane)
# 7th chords, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# DRUMS (Bars 2-4)
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5, cutoff=0.25)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

# SAX (Dante)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (start on 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.125),  # F#
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.375),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.375, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),    # A
    # Bar 3 (leave it hanging)
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.625),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.625, end=3.875),  # B
    # Bar 4 (come back and finish it)
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),     # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),     # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),     # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),     # F
    pretty_midi.Note(velocity=110, pitch=70, start=5.5, end=5.75),     # A#
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),     # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
