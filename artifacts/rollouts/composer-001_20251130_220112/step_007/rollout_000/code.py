
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm, chromatic approaches
# Fm: F, Ab, D, C
# Walking bass line (F, Gb, Ab, A, Bb, B, C, Db, D, Eb, E, F#, F, Gb, Ab, A)
# Using note numbers: F=53, Gb=54, Ab=56, A=57, Bb=58, B=59, C=60, Db=61,
# D=62, Eb=63, E=64, F#=65

bass_notes = [
    (53, 1.5), (54, 1.5), (56, 1.5), (57, 1.5), (58, 1.5), (59, 1.5), (60, 1.5), (61, 1.5),
    (62, 1.5), (63, 1.5), (64, 1.5), (65, 1.5), (53, 1.5), (54, 1.5), (56, 1.5), (57, 1.5),
    (58, 1.5), (59, 1.5), (60, 1.5), (61, 1.5), (62, 1.5), (63, 1.5), (64, 1.5), (65, 1.5),
    (53, 1.5), (54, 1.5), (56, 1.5), (57, 1.5), (58, 1.5), (59, 1.5), (60, 1.5), (61, 1.5)
]

for note_info in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_info[0], start=note_info[1], end=note_info[1] + 0.25)
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4, comp on 2 and 4
# In Fm: F7 (F, Ab, C, Eb), Bb7 (Bb, D, F, Ab), Eb7 (Eb, Gb, Bb, Db), Ab7 (Ab, B, Db, E)
# Chord positions: root, 7, 5, 3

# Bar 2: 2nd beat, F7
# Bar 3: 2nd beat, Bb7
# Bar 4: 2nd beat, Eb7

chord_notes = [
    # Bar 2 (1.5 - 2.0s) - F7 on 2nd beat (1.875s)
    (53, 1.875), (60, 1.875), (64, 1.875), (63, 1.875),
    # Bar 3 (2.5 - 3.0s) - Bb7 on 2nd beat (2.875s)
    (58, 2.875), (62, 2.875), (60, 2.875), (63, 2.875),
    # Bar 4 (3.5 - 4.0s) - Eb7 on 2nd beat (3.875s)
    (63, 3.875), (66, 3.875), (58, 3.875), (61, 3.875),
    # Add some comping (1.5s to 3.5s)
    (53, 1.5), (63, 1.5), (60, 1.5), (63, 1.5),
    (58, 2.0), (63, 2.0), (60, 2.0), (63, 2.0),
    (63, 2.5), (66, 2.5), (58, 2.5), (61, 2.5),
    (53, 3.0), (63, 3.0), (60, 3.0), (63, 3.0),
    (58, 3.5), (63, 3.5), (60, 3.5), (63, 3.5)
]

for note_info in chord_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_info[0], start=note_info[1], end=note_info[1] + 0.25)
    piano.notes.append(note)

# Sax (Dante) - motif: F, Ab, C, Eb (Fm7), then Ab, Bb, D, F (Ab7) - 1 bar
# Then repeat the motif, but leave it hanging on D (beat 3) and resolve on F (beat 4)

sax_notes = [
    # Bar 2 (1.5 - 2.0s)
    (53, 1.5), (56, 1.5), (60, 1.5), (63, 1.5), (56, 1.5), (58, 1.5), (62, 1.5), (53, 1.5),
    # Bar 3 (2.5 - 3.0s)
    (56, 2.5), (58, 2.5), (62, 2.5), (53, 2.5), (56, 2.5), (58, 2.5), (62, 2.5), (53, 2.5),
    # Bar 4 (3.5 - 4.0s)
    (56, 3.5), (58, 3.5), (62, 3.5), (53, 3.5)
]

for note_info in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note_info[0], start=note_info[1], end=note_info[1] + 0.25)
    sax.notes.append(note)

# Add remaining bars with rest
# Bar 5 (4.5 - 6.0s): everyone rests

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
