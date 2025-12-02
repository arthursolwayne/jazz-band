
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
start_time = 1.5
bar_length = 1.5

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=start_time, end=start_time + 0.375),
    pretty_midi.Note(velocity=90, pitch=50, start=start_time + 0.375, end=start_time + 0.75),
    pretty_midi.Note(velocity=90, pitch=51, start=start_time + 0.75, end=start_time + 1.125),
    pretty_midi.Note(velocity=90, pitch=53, start=start_time + 1.125, end=start_time + 1.5),
    pretty_midi.Note(velocity=90, pitch=55, start=start_time + 1.5, end=start_time + 1.875),
    pretty_midi.Note(velocity=90, pitch=57, start=start_time + 1.875, end=start_time + 2.25),
    pretty_midi.Note(velocity=90, pitch=58, start=start_time + 2.25, end=start_time + 2.625),
    pretty_midi.Note(velocity=90, pitch=60, start=start_time + 2.625, end=start_time + 3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=start_time + 3.0, end=start_time + 3.375),
    pretty_midi.Note(velocity=90, pitch=63, start=start_time + 3.375, end=start_time + 3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=start_time + 3.75, end=start_time + 4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=start_time + 4.125, end=start_time + 4.5),
    pretty_midi.Note(velocity=90, pitch=68, start=start_time + 4.5, end=start_time + 4.875),
    pretty_midi.Note(velocity=90, pitch=70, start=start_time + 4.875, end=start_time + 5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=start_time + 5.25, end=start_time + 5.625),
    pretty_midi.Note(velocity=90, pitch=73, start=start_time + 5.625, end=start_time + 6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, C, Eb
# Bb7: Bb, Db, F, Ab
# Eb7: Eb, Gb, Bb, Db
# Ab7: Ab, B, Eb, Gb
chord_times = [
    start_time + 1.125,  # 2nd beat of bar 2
    start_time + 3.375,  # 2nd beat of bar 3
    start_time + 5.625   # 2nd beat of bar 4
]
chords = [
    [76, 88, 72, 74],  # Fm7
    [79, 82, 76, 88],  # Bb7
    [74, 78, 79, 82]   # Eb7
]
for i, chord in enumerate(chords):
    for note in chord:
        n = pretty_midi.Note(velocity=100, pitch=note, start=chord_times[i], end=chord_times[i] + 0.375)
        piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    bar_start = start_time + bar * bar_length
    for beat in range(4):
        time = bar_start + beat * bar_length / 4
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4)
            drums.notes.append(note)
            note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 4)
            drums.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - C - Eb (Fm7) over 2 bars, then repeat with Ab - C - Eb - F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=start_time, end=start_time + 0.375),
    pretty_midi.Note(velocity=110, pitch=88, start=start_time + 0.375, end=start_time + 0.75),
    pretty_midi.Note(velocity=110, pitch=72, start=start_time + 0.75, end=start_time + 1.125),
    pretty_midi.Note(velocity=110, pitch=74, start=start_time + 1.125, end=start_time + 1.5),
    pretty_midi.Note(velocity=110, pitch=88, start=start_time + 1.5, end=start_time + 1.875),
    pretty_midi.Note(velocity=110, pitch=72, start=start_time + 1.875, end=start_time + 2.25),
    pretty_midi.Note(velocity=110, pitch=74, start=start_time + 2.25, end=start_time + 2.625),
    pretty_midi.Note(velocity=110, pitch=76, start=start_time + 2.625, end=start_time + 3.0),
    pretty_midi.Note(velocity=110, pitch=88, start=start_time + 3.0, end=start_time + 3.375),
    pretty_midi.Note(velocity=110, pitch=72, start=start_time + 3.375, end=start_time + 3.75),
    pretty_midi.Note(velocity=110, pitch=74, start=start_time + 3.75, end=start_time + 4.125),
    pretty_midi.Note(velocity=110, pitch=76, start=start_time + 4.125, end=start_time + 4.5),
    pretty_midi.Note(velocity=110, pitch=88, start=start_time + 4.5, end=start_time + 4.875),
    pretty_midi.Note(velocity=110, pitch=72, start=start_time + 4.875, end=start_time + 5.25),
    pretty_midi.Note(velocity=110, pitch=74, start=start_time + 5.25, end=start_time + 5.625),
    pretty_midi.Note(velocity=110, pitch=76, start=start_time + 5.625, end=start_time + 6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dantes_intro.mid")
