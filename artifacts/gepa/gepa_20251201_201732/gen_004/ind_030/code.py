
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
drum_notes = []
for i in range(4):  # 4 beats per bar
    # Kick on 1 and 3
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=i * 0.375, end=i * 0.375 + 0.1))
    # Snare on 2 and 4
    if i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=i * 0.375, end=i * 0.375 + 0.1))
    # Hi-hat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=i * 0.375 + 0.05))
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (F2, G2, Ab2, A2) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.5 + 0.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=1.875 + 0.375),  # G2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.25 + 0.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=2.625 + 0.375),  # A2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chords each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.15),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.15),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.5 + 0.15),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.15),  # Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=1.875 + 0.15),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=1.875 + 0.15),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=1.875 + 0.15),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=1.875 + 0.15),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.25 + 0.15),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.25 + 0.15),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.25 + 0.15),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.25 + 0.15),  # Bb
])
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# A simple motif: F, Ab, Bb, C, then repeat but finish with G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.5 + 0.15),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.65, end=1.65 + 0.15),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.8, end=1.8 + 0.15),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.95, end=1.95 + 0.15),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.25 + 0.15),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.4, end=2.4 + 0.15),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.55, end=2.55 + 0.15),  # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=2.7, end=2.7 + 0.15),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue (3.0 - 4.5s)
# Same pattern as Bar 1
for i in range(4):  # 4 beats per bar
    # Kick on 1 and 3
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.1))
    # Snare on 2 and 4
    if i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.1))
    # Hi-hat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.05))
drums.notes.extend(drum_notes)

# Bar 4: Drums continue (4.5 - 6.0s)
for i in range(4):  # 4 beats per bar
    # Kick on 1 and 3
    if i == 0 or i == 2:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.1))
    # Snare on 2 and 4
    if i == 1 or i == 3:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.1))
    # Hi-hat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.05))
drums.notes.extend(drum_notes)

# Bar 3: Bass continues (3.0 - 4.5s)
# Walking line: Bb2, C2, Db2, D2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.0 + 0.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.375 + 0.375),  # C2
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=3.75 + 0.375),  # Db2
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.125 + 0.375),  # D2
]
bass.notes.extend(bass_notes)

# Bar 4: Bass continues (4.5 - 6.0s)
# Walking line: C2, D2, Eb2, F2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.5 + 0.375),  # C2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=4.875 + 0.375),  # D2
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.25 + 0.375),  # Eb2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=5.625 + 0.375),  # F2
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues (3.0 - 4.5s)
# D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.15),  # D
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.0 + 0.15),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.0 + 0.15),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.0 + 0.15),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Piano continues (4.5 - 6.0s)
# Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.15),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.15),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.5 + 0.15),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.15),  # Eb
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("f_minor_intro.mid")
