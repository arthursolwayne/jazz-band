
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full band in (1.5 - 3.0s)
# Bass: F2 (D2 is not in Fm, using F2 as root)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),   # F2 (root) on 1
    pretty_midi.Note(velocity=90, pitch=56, start=1.875, end=2.25),  # C3 (fifth) on 2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # D#2 (chromatic approach) on 3
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0)    # F2 (root) on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.75)    # Ab
]
piano.notes.extend(piano_notes_bar2)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.5)    # Ab
]
piano.notes.extend(piano_notes_bar3)

# Bar 4: C7 (C, E, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=58, start=2.75, end=3.0)    # Bb
]
piano.notes.extend(piano_notes_bar4)

# Sax: Motif in Fm, one phrase, incomplete, then resolved
# Motif: F, Ab, D, Eb (melodic approach to Fm)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=1.625, end=1.75), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=53, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=56, start=2.625, end=2.75), # C
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=2.875), # E
    pretty_midi.Note(velocity=110, pitch=58, start=2.875, end=3.0)   # Ab
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 8th notes
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
