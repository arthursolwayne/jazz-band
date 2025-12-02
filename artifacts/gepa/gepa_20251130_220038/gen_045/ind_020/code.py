
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42, 42, 42, 42]

for i, note in enumerate(kick_notes):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75, end=bar1_start + i * 0.75 + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    snare = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75 + 0.1875, end=bar1_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    62, 64, 63, 61,
    # Bar 3
    61, 62, 64, 63,
    # Bar 4
    63, 61, 62, 64
]
for i, note in enumerate(bass_notes):
    start_time = 1.5 + i * 0.375
    end_time = start_time + 0.25
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start_time, end=end_time)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (62, 1.5), (64, 1.5), (67, 1.5), (69, 1.5),
    # Bar 3: G7 (G, B, D, F)
    (67, 2.25), (71, 2.25), (69, 2.25), (64, 2.25),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 3.0), (62, 3.0), (67, 3.0), (62, 3.0)
]
for pitch, start in piano_notes:
    end = start + 0.25
    piano_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing.
sax_notes = [
    # Bar 2
    (67, 1.5, 0.5),  # D
    (69, 2.0, 0.5),  # F
    (67, 2.5, 0.5),  # D
    (69, 3.0, 0.5),  # F
    # Bar 3
    (66, 3.5, 0.5),  # C
    (67, 4.0, 0.5),  # D
    (69, 4.5, 0.5),  # F
    # Bar 4
    (67, 5.0, 0.5),  # D
    (69, 5.5, 0.5)   # F
]
for pitch, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums: Continue for Bars 2-4
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42, 42, 42, 42]

    for i, note in enumerate(kick_notes):
        kick = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + i * 0.75, end=bar_start + i * 0.75 + 0.375)
        drums.notes.append(kick)

    for i, note in enumerate(snare_notes):
        snare = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + i * 0.75 + 0.1875, end=bar_start + i * 0.75 + 0.1875 + 0.375)
        drums.notes.append(snare)

    for i, note in enumerate(hihat_notes):
        hihat = pretty_midi.Note(velocity=80, pitch=note, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
