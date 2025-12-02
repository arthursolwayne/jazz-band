
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar at 120 BPM

# Drums - Bar 1
kick_notes = [36] * 2
snare_notes = [38] * 2
hihat_notes = [42] * 8

for i in range(2):
    kick_time = i * bar_length + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

    snare_time = i * bar_length + 0.75
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

    for j in range(8):
        hihat_time = i * bar_length + j * 0.1875
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Walking line with chromatic approaches
bass_notes = [
    (36, 1.5), (37, 1.75), (38, 2.0), (39, 2.25),
    (40, 2.5), (41, 2.75), (42, 3.0), (43, 3.25),
    (44, 3.5), (45, 3.75), (46, 4.0), (47, 4.25),
    (48, 4.5), (49, 4.75), (50, 5.0), (51, 5.25)
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    (60, 2.0, 0.25), (64, 2.0, 0.25), (67, 2.0, 0.25), (71, 2.0, 0.25),
    (60, 4.0, 0.25), (64, 4.0, 0.25), (67, 4.0, 0.25), (71, 4.0, 0.25)
]
for pitch, time, duration in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Sax - Motif: C - E - G - Bb (hanging on Bb)
sax_notes = [
    (60, 1.5, 0.25), (64, 1.75, 0.25), (67, 2.0, 0.25), (69, 2.25, 0.25),
    (69, 3.0, 0.25), (67, 3.25, 0.25), (64, 3.5, 0.25), (60, 3.75, 0.25)
]
for pitch, time, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Drums - Bars 2-4
for i in range(3):
    bar_start = 1.5 + i * bar_length
    for j in range(2):
        kick_time = bar_start + j * bar_length + 0.0
        kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick)

        snare_time = bar_start + j * bar_length + 0.75
        snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare)

        for k in range(8):
            hihat_time = bar_start + j * bar_length + k * 0.1875
            hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
