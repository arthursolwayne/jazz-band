
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line starting on F, chromatic approach to G, then root
bass_notes = [
    (45, 1.5), (46, 1.875), (44, 2.25), (45, 2.625),  # F, F#, Eb, F
    (47, 3.0), (48, 3.375), (46, 3.75), (47, 4.125),  # G, G#, F, G
    (48, 4.5), (49, 4.875), (47, 5.25), (48, 5.625)   # G#, A, G, G#
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4, F7, Bb7, F7, Bb7
piano_notes = []
chords = [
    [(57, 1.875), (60, 1.875), (62, 1.875), (64, 1.875)],  # F7
    [(55, 3.375), (58, 3.375), (60, 3.375), (62, 3.375)],  # Bb7
    [(57, 4.875), (60, 4.875), (62, 4.875), (64, 4.875)],  # F7
    [(55, 6.375), (58, 6.375), (60, 6.375), (62, 6.375)]   # Bb7
]
for chord in chords:
    for note, time in chord:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif starting on F, short and singing, leaves it hanging
sax_notes = [
    (57, 1.5), (59, 1.875), (60, 2.25), (57, 2.625),
    (59, 3.0), (60, 3.375), (57, 3.75), (59, 4.125),
    (60, 4.5), (57, 4.875), (59, 5.25), (60, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick1 = (36, bar_start)
    snare2 = (38, bar_start + 0.375)
    hihat2 = (42, bar_start + 0.375)
    kick3 = (36, bar_start + 0.75)
    snare4 = (38, bar_start + 1.125)
    hihat4 = (42, bar_start + 1.125)
    kick1_next = (36, bar_start + 1.5)
    snare2_next = (38, bar_start + 1.875)
    hihat2_next = (42, bar_start + 1.875)
    kick3_next = (36, bar_start + 2.25)
    snare4_next = (38, bar_start + 2.625)
    hihat4_next = (42, bar_start + 2.625)

    drum_notes.extend([kick1, snare2, hihat2, kick3, snare4, hihat4,
                       kick1_next, snare2_next, hihat2_next, kick3_next, snare4_next, hihat4_next])

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
