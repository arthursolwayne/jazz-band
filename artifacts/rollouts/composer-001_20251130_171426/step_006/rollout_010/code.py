
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
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    start = bar1_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar1_start + (i * 0.75) + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar1_start + (i * 0.125)
    hihat = pretty_midi.Note(velocity=70, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    64, 65, 67, 69,  # Bar 2
    69, 70, 72, 71,  # Bar 3
    71, 69, 67, 64   # Bar 4
]
bass_durations = [0.375] * 12
bass_start = 1.5
for i, note in enumerate(bass_notes):
    start = bass_start + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + bass_durations[i])
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    64, 67, 71, 72,  # F7
    # Bar 3
    64, 67, 70, 72,  # F7
    # Bar 4
    64, 67, 71, 72,  # F7
]
piano_durations = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
piano_start = 1.5
for i, note in enumerate(piano_notes):
    start = piano_start + (i * 0.5)
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + piano_durations[i])
    piano.notes.append(piano_note)

# Sax: short motif, starts on beat 1, leaves it hanging
sax_notes = [
    64,  # F
    67,  # A
    69,  # Bb
    64   # F
]
sax_durations = [0.5, 0.5, 0.5, 0.5]
sax_start = 1.5
for i, note in enumerate(sax_notes):
    start = sax_start + (i * 0.5)
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + sax_durations[i])
    sax.notes.append(sax_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

for start in [bar2_start, bar3_start, bar4_start]:
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8

    for i, note in enumerate(kick_notes):
        kick_start = start + (i * 0.75)
        kick = pretty_midi.Note(velocity=100, pitch=note, start=kick_start, end=kick_start + 0.375)
        drums.notes.append(kick)

    for i, note in enumerate(snare_notes):
        snare_start = start + (i * 0.75) + 0.1875
        snare = pretty_midi.Note(velocity=110, pitch=note, start=snare_start, end=snare_start + 0.375)
        drums.notes.append(snare)

    for i, note in enumerate(hihat_notes):
        hihat_start = start + (i * 0.125)
        hihat = pretty_midi.Note(velocity=70, pitch=note, start=hihat_start, end=hihat_start + 0.125)
        drums.notes.append(hihat)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_moment.mid")
