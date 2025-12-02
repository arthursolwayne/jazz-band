
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

kick_times = [0.0, 1.5]
snare_times = [0.75, 2.25]
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]

for note, time in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15)
    drums.notes.append(kick)

for note, time in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

for note, time in zip(hihat_notes, hihat_times):
    hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(hihat)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking line, chromatic approaches, no repeated notes
# C minor blues scale: C Eb F Gb G Bb
# Walking bass line in C minor (key is C minor)
bass_notes = [60, 62, 63, 61, 62, 63, 64, 62, 60, 62, 63, 64, 62, 63, 64, 62]
bass_times = [1.5 + i * 0.375 for i in range(len(bass_notes))]
for note, time in zip(bass_notes, bass_times):
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Diane - 7th chords, comp on 2 and 4
# Cm7, F7, Bbm7, Eb7
piano_notes = [
    # Cm7 (C, Eb, G, Bb) on beat 2
    (60, 2.25), (64, 2.25), (67, 2.25), (69, 2.25),
    # F7 (F, A, C, Eb) on beat 4
    (65, 3.75), (68, 3.75), (72, 3.75), (76, 3.75),
    # Cm7 (C, Eb, G, Bb) on beat 2
    (60, 5.25), (64, 5.25), (67, 5.25), (69, 5.25),
    # F7 (F, A, C, Eb) on beat 4
    (65, 6.75), (68, 6.75), (72, 6.75), (76, 6.75)
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(piano_note)

# Dante - Tenor sax: one short motif, make it sing
# Start it, leave it hanging, come back and finish it
# Cm scale: C Eb F Gb G Bb
# Motif: C - Eb - Gb - G, then repeat
sax_notes = [
    (60, 1.5), (64, 1.5), (67, 1.5), (68, 1.5),
    (60, 2.5), (64, 2.5), (67, 2.5), (68, 2.5)
]
sax_times = [
    1.5, 1.875, 2.25, 2.625,
    2.5, 2.875, 3.25, 3.625
]
for note, time in zip(sax_notes, sax_times):
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(sax_note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
