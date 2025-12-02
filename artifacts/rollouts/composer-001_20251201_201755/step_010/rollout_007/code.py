
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm (F2, Ab2, D2, G2), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # G2
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),   # Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes_bar2)

# Sax: Motif - short, singable, leaves it hanging
sax_notes_bar2 = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # Ab (Fm7)
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # Bb (chromatic)
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=2.75),  # E (suspense)
]
sax.notes.extend(sax_notes_bar2)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Fm (F2, Ab2, D2, G2)
bass_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # G2
]
bass.notes.extend(bass_notes_bar3)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),   # Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes_bar3)

# Sax: Motif continuation, finish it
sax_notes_bar3 = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # F
]
sax.notes.extend(sax_notes_bar3)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
]
drums.notes.extend(drum_notes_bar4)

# Bass: Walking line in Fm (F2, Ab2, D2, G2)
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes_bar4)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),   # Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes_bar4)

# Sax: Motif resolution, leave a space
sax_notes_bar4 = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
