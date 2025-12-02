
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
bar_1_start = 0.0
bar_1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i in range(2):
    kick = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=bar_1_start + i * 0.75, end=bar_1_start + i * 0.75 + 0.375)
    drums.notes.append(kick)
    snare = pretty_midi.Note(velocity=110, pitch=snare_notes[i], start=bar_1_start + i * 0.75 + 0.375, end=bar_1_start + i * 0.75 + 0.375 + 0.375)
    drums.notes.append(snare)

for i in range(8):
    hihat = pretty_midi.Note(velocity=90, pitch=hihat_notes[i], start=bar_1_start + i * 0.375, end=bar_1_start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5), (40, 1.875), (38, 2.25), (43, 2.625),
    (43, 2.625), (45, 2.875), (43, 3.25), (38, 3.625),
    (38, 3.625), (40, 3.875), (38, 4.25), (43, 4.625),
    (43, 4.625), (45, 4.875), (43, 5.25), (38, 5.625)
]
for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
# Bar 3: Gm7 (G Bb D F)
# Bar 4: Cmaj7 (C E G B)
bar_2_chord = [62, 66, 69, 64]  # D7
bar_3_chord = [67, 70, 69, 64]  # Gm7
bar_4_chord = [60, 64, 67, 71]  # Cmaj7

# Comp on 2 and 4
for bar, chord in enumerate([bar_2_chord, bar_3_chord, bar_4_chord], start=2):
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=(bar - 1) * 1.5 + 0.75, end=(bar - 1) * 1.5 + 0.75 + 0.375)
        piano.notes.append(note)

# You: Tenor sax (melody)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5), (64, 1.875), (62, 2.25), (60, 2.625),
    (62, 3.25), (64, 3.625), (62, 4.25), (60, 4.625),
    (62, 5.25), (64, 5.625)
]
for pitch, start in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
