
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax melody: C - E - G - B (Cmaj7 arpeggio, one note per beat)
sax_notes = [
    (60, 1.5, 0.375),  # C
    (64, 1.875, 0.375), # E
    (67, 2.25, 0.375),  # G
    (71, 2.625, 0.375)  # B
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bass line: walking line in C, chromatic approach to C
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (64, 2.625, 0.375)  # E
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (60, 1.875, 0.375),  # C
    (64, 1.875, 0.375),  # E
    (67, 1.875, 0.375),  # G
    (71, 1.875, 0.375),  # B
    (60, 2.625, 0.375),  # C
    (64, 2.625, 0.375),  # E
    (67, 2.625, 0.375),  # G
    (71, 2.625, 0.375)   # B
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Bar 3: Drums continue
for i in range(3):
    start = 1.5 + i * 1.5
    drum_notes = [
        (36, start, 0.375),  # Kick on 1
        (42, start, 0.1875), # Hihat on 1
        (38, start + 0.375, 0.375), # Snare on 2
        (42, start + 0.375, 0.1875), # Hihat on 2
        (36, start + 0.75, 0.375),  # Kick on 3
        (42, start + 0.75, 0.1875), # Hihat on 3
        (38, start + 1.125, 0.375), # Snare on 4
        (42, start + 1.125, 0.1875) # Hihat on 4
    ]
    for note, s, d in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d)
        drums.notes.append(dr)

# Bar 3: Sax continues with motif variation (C - E - G - B - C)
sax_notes = [
    (60, 3.0, 0.375),  # C
    (64, 3.375, 0.375), # E
    (67, 3.75, 0.375),  # G
    (71, 4.125, 0.375), # B
    (60, 4.5, 0.375)    # C
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Bass walking line
bass_notes = [
    (60, 3.0, 0.375),  # C
    (61, 3.375, 0.375), # C#
    (62, 3.75, 0.375),  # D
    (64, 4.125, 0.375), # E
    (65, 4.5, 0.375)    # F
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Bar 3: Piano 7th chords on 2 and 4
piano_notes = [
    (60, 3.375, 0.375),  # C
    (64, 3.375, 0.375),  # E
    (67, 3.375, 0.375),  # G
    (71, 3.375, 0.375),  # B
    (60, 4.125, 0.375),  # C
    (64, 4.125, 0.375),  # E
    (67, 4.125, 0.375),  # G
    (71, 4.125, 0.375)   # B
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Bar 4: Drums continue
for i in range(3):
    start = 1.5 + i * 1.5
    drum_notes = [
        (36, start, 0.375),  # Kick on 1
        (42, start, 0.1875), # Hihat on 1
        (38, start + 0.375, 0.375), # Snare on 2
        (42, start + 0.375, 0.1875), # Hihat on 2
        (36, start + 0.75, 0.375),  # Kick on 3
        (42, start + 0.75, 0.1875), # Hihat on 3
        (38, start + 1.125, 0.375), # Snare on 4
        (42, start + 1.125, 0.1875) # Hihat on 4
    ]
    for note, s, d in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d)
        drums.notes.append(dr)

# Bar 4: Sax ends with resolution (C - B - G - E)
sax_notes = [
    (60, 4.5, 0.375),  # C
    (71, 4.875, 0.375), # B
    (67, 5.25, 0.375),  # G
    (64, 5.625, 0.375)  # E
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 4: Bass walking line
bass_notes = [
    (60, 4.5, 0.375),  # C
    (61, 4.875, 0.375), # C#
    (62, 5.25, 0.375),  # D
    (64, 5.625, 0.375)  # E
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Bar 4: Piano 7th chords on 2 and 4
piano_notes = [
    (60, 4.875, 0.375),  # C
    (64, 4.875, 0.375),  # E
    (67, 4.875, 0.375),  # G
    (71, 4.875, 0.375),  # B
    (60, 5.625, 0.375),  # C
    (64, 5.625, 0.375),  # E
    (67, 5.625, 0.375),  # G
    (71, 5.625, 0.375)   # B
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
