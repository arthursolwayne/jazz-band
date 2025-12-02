
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking, chromatic approaches)
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (61, 2.25, 0.375),  # C
    (60, 2.625, 0.375), # Bb
    (62, 3.0, 0.375),   # D
    (63, 3.375, 0.375), # Eb
    (61, 3.75, 0.375),  # C
    (60, 4.125, 0.375), # Bb
    (62, 4.5, 0.375),   # D
    (63, 4.875, 0.375), # Eb
    (61, 5.25, 0.375),  # C
    (60, 5.625, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    (62, 1.875, 0.1875), # D
    (67, 1.875, 0.1875), # G
    (64, 1.875, 0.1875), # Bb
    (69, 1.875, 0.1875), # C
    (62, 2.625, 0.1875),
    (67, 2.625, 0.1875),
    (64, 2.625, 0.1875),
    (69, 2.625, 0.1875),
    # Bar 3: Dm7 on 2 and 4
    (62, 3.375, 0.1875),
    (67, 3.375, 0.1875),
    (64, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    (62, 4.125, 0.1875),
    (67, 4.125, 0.1875),
    (64, 4.125, 0.1875),
    (69, 4.125, 0.1875),
    # Bar 4: Dm7 on 2 and 4
    (62, 4.875, 0.1875),
    (67, 4.875, 0.1875),
    (64, 4.875, 0.1875),
    (69, 4.875, 0.1875),
    (62, 5.625, 0.1875),
    (67, 5.625, 0.1875),
    (64, 5.625, 0.1875),
    (69, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes.append((36, bar_start, 0.375))     # Kick on 1
    drum_notes.append((38, bar_start + 0.375, 0.375)) # Snare on 2
    drum_notes.append((36, bar_start + 0.75, 0.375))  # Kick on 3
    drum_notes.append((38, bar_start + 1.125, 0.375)) # Snare on 4
    for i in range(8):
        drum_notes.append((42, bar_start + i * 0.1875, 0.1875))  # Hi-hat on every eighth

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Tenor Sax (short motif, make it sing)
sax_notes = [
    (62, 1.5, 0.25),   # D
    (64, 1.75, 0.25),  # Eb
    (62, 2.0, 0.25),   # D
    (64, 2.25, 0.25),  # Eb
    (62, 3.0, 0.25),   # D
    (64, 3.25, 0.25),  # Eb
    (62, 4.5, 0.25),   # D
    (64, 4.75, 0.25)   # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
