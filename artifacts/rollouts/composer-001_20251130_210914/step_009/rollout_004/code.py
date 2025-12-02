
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
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42] * 8
drum_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]

for i in range(4):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=drum_times[i], end=drum_times[i] + 0.125)
    snare = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=drum_times[i + 4], end=drum_times[i + 4] + 0.125)
    for j in range(2):
        hihat = pretty_midi.Note(velocity=90, pitch=hihat_notes[j], start=drum_times[j + i * 4], end=drum_times[j + i * 4] + 0.125)
    drums.notes.extend([kick, snare, hihat, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeating notes
bass_notes = [57, 55, 53, 51, 50, 52, 53, 55, 57, 55, 53, 51, 50, 52, 53, 55]
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]
for i in range(len(bass_notes)):
    note = pretty_midi.Note(velocity=80, pitch=bass_notes[i], start=bass_times[i], end=bass_times[i] + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    [60, 64, 67],  # C7 on beat 2
    [62, 65, 68],  # D7 on beat 4
    [60, 64, 67],  # C7 on beat 2
    [62, 65, 68],  # D7 on beat 4
    [60, 64, 67],  # C7 on beat 2
    [62, 65, 68],  # D7 on beat 4
]
piano_times = [2.0, 2.375, 2.75, 3.125, 3.5, 3.875, 4.25, 4.625, 5.0, 5.375, 5.75, 6.125]
for i in range(len(piano_notes)):
    for note in piano_notes[i]:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=piano_times[i], end=piano_times[i] + 0.125)
        piano.notes.append(piano_note)

# Sax: Motif (Bb, Ab, Gb, F), repeat at bar 3 and resolve at bar 4
sax_notes = [100, 98, 96, 95, 100, 98, 96, 95, 100, 98, 96, 95, 100, 98, 96, 95]
sax_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]
for i in range(len(sax_notes)):
    note = pretty_midi.Note(velocity=100, pitch=sax_notes[i], start=sax_times[i], end=sax_times[i] + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
