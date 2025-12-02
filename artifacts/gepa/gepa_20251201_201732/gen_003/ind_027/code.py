
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),   # D2 on 1
    (42, 1.875, 0.375), # F2 on 2
    (40, 2.25, 0.375),  # Eb2 on 3
    (43, 2.625, 0.375), # G2 on 4
    (42, 3.0, 0.375),   # F2 on 1
    (44, 3.375, 0.375), # Ab2 on 2
    (41, 3.75, 0.375),  # E2 on 3
    (43, 4.125, 0.375), # G2 on 4
    (40, 4.5, 0.375),   # Eb2 on 1
    (42, 4.875, 0.375), # F2 on 2
    (43, 5.25, 0.375),  # G2 on 3
    (45, 5.625, 0.375)  # Bb2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# F7 (F A C Eb), Bb7 (Bb D F Ab), E7 (E G# B D), A7 (A C# E G)
piano_notes = [
    (65, 1.5, 0.375), (69, 1.5, 0.375), (67, 1.5, 0.375), (62, 1.5, 0.375),  # F7 on 1
    (71, 1.875, 0.375), (74, 1.875, 0.375), (72, 1.875, 0.375), (67, 1.875, 0.375),  # Bb7 on 2
    (69, 2.25, 0.375), (73, 2.25, 0.375), (71, 2.25, 0.375), (68, 2.25, 0.375),  # E7 on 3
    (69, 2.625, 0.375), (74, 2.625, 0.375), (72, 2.625, 0.375), (67, 2.625, 0.375),  # A7 on 4
    (65, 3.0, 0.375), (69, 3.0, 0.375), (67, 3.0, 0.375), (62, 3.0, 0.375),  # F7 on 1
    (71, 3.375, 0.375), (74, 3.375, 0.375), (72, 3.375, 0.375), (67, 3.375, 0.375),  # Bb7 on 2
    (69, 3.75, 0.375), (73, 3.75, 0.375), (71, 3.75, 0.375), (68, 3.75, 0.375),  # E7 on 3
    (69, 4.125, 0.375), (74, 4.125, 0.375), (72, 4.125, 0.375), (67, 4.125, 0.375),  # A7 on 4
    (65, 4.5, 0.375), (69, 4.5, 0.375), (67, 4.5, 0.375), (62, 4.5, 0.375),  # F7 on 1
    (71, 4.875, 0.375), (74, 4.875, 0.375), (72, 4.875, 0.375), (67, 4.875, 0.375),  # Bb7 on 2
    (69, 5.25, 0.375), (73, 5.25, 0.375), (71, 5.25, 0.375), (68, 5.25, 0.375),  # E7 on 3
    (69, 5.625, 0.375), (74, 5.625, 0.375), (72, 5.625, 0.375), (67, 5.625, 0.375)   # A7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# You: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (66, 1.5, 0.375),  # F on 1
    (69, 1.875, 0.375), # A on 2
    (67, 2.25, 0.375),  # G on 3
    (62, 2.625, 0.375), # Eb on 4
    (66, 3.0, 0.375),   # F on 1
    (69, 3.375, 0.375), # A on 2
    (67, 3.75, 0.375),  # G on 3
    (62, 4.125, 0.375), # Eb on 4
    (66, 4.5, 0.375),   # F on 1
    (69, 4.875, 0.375), # A on 2
    (67, 5.25, 0.375),  # G on 3
    (62, 5.625, 0.375)  # Eb on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):  # Bars 2, 3, 4
    for beat in [0, 1, 2, 3]:
        start = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append((36, start, 0.375))  # Kick
        if beat == 1 or beat == 3:
            drum_notes.append((38, start, 0.375))  # Snare
        drum_notes.append((42, start, 0.375))  # Hihat
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
