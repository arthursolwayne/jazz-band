
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
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),  # 1
    (36, 0.75), (38, 1.125), (42, 1.125), # 2
    (36, 1.5), (38, 1.875), (42, 1.875),  # 3
    (36, 2.25), (38, 2.625), (42, 2.625)  # 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: F2 (D2) - F2 - G2 - F2 (walking line with chromatic approach)
bass_notes = [
    (38, 1.5), (39, 1.75), (40, 2.0), (38, 2.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (53, 1.5), (60, 1.5), (64, 1.5), (65, 1.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Motif - F (53) - Ab (56) - C (57) - rest
sax_notes = [
    (53, 1.5), (56, 1.75), (57, 2.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full ensemble (3.0 - 4.5s)
# Bass: Ab2 (Eb2) - Bb2 (F2) - C2 (G2) - Ab2 (Eb2) (walking line with chromatic approach)
bass_notes = [
    (40, 3.0), (41, 3.25), (42, 3.5), (40, 3.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Dm7 (D, F, A, C)
piano_notes = [
    (50, 3.0), (52, 3.0), (55, 3.0), (57, 3.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Motif continuation - rest - F (53) - Ab (56) - C (57)
sax_notes = [
    (53, 3.5), (56, 3.75), (57, 4.0)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full ensemble (4.5 - 6.0s)
# Bass: Bb2 (F2) - C2 (G2) - D2 (A2) - Bb2 (F2) (walking line with chromatic approach)
bass_notes = [
    (41, 4.5), (42, 4.75), (44, 5.0), (41, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    (55, 4.5), (57, 4.5), (60, 4.5), (62, 4.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Sax: Motif final - rest - F (53) - Ab (56) - C (57) - resolution
sax_notes = [
    (53, 5.0), (56, 5.25), (57, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
