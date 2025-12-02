
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on beat 1
    (38, 0.75, 0.375), # Snare on beat 2
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.375, 0.1875),
    (42, 0.75, 0.1875),
    (42, 1.125, 0.1875),
    (36, 1.5, 0.375),  # Kick on beat 3
    (38, 1.875, 0.375), # Snare on beat 4
    (42, 1.5, 0.1875), # Hihat on 3 & 4
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm
bass_notes = [
    (43, 1.5, 0.375), # F
    (41, 1.875, 0.375), # D
    (40, 2.25, 0.375), # C
    (41, 2.625, 0.375), # D
    (43, 3.0, 0.375), # F
    (45, 3.375, 0.375), # Ab
    (44, 3.75, 0.375), # G
    (43, 4.125, 0.375), # F
    (45, 4.5, 0.375), # Ab
    (44, 4.875, 0.375), # G
    (46, 5.25, 0.375), # A
    (45, 5.625, 0.375) # Ab
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano comping - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (55, 1.875, 0.375), # F7: F, A, C, Eb
    (53, 1.875, 0.375),
    (50, 1.875, 0.375),
    (48, 1.875, 0.375),
    # Bar 3
    (55, 3.375, 0.375),
    (53, 3.375, 0.375),
    (50, 3.375, 0.375),
    (48, 3.375, 0.375),
    # Bar 4
    (55, 5.625, 0.375),
    (53, 5.625, 0.375),
    (50, 5.625, 0.375),
    (48, 5.625, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax - 4-bar motif in Fm, short and memorable
sax_notes = [
    (59, 1.5, 0.5), # F (beat 1)
    (62, 2.25, 0.5), # Ab (beat 3)
    (60, 2.625, 0.5), # G (beat 4)
    (59, 3.0, 0.5), # F (beat 1)
    (62, 3.75, 0.5), # Ab (beat 3)
    (60, 4.125, 0.5), # G (beat 4)
    (59, 4.5, 0.5), # F (beat 1)
    (62, 5.25, 0.5), # Ab (beat 3)
    (60, 5.625, 0.5) # G (beat 4)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4 (full pattern)
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start, 0.375),  # Kick on beat 1
        (38, start + 0.75, 0.375), # Snare on beat 2
        (42, start, 0.1875), # Hihat on 1 & 2
        (42, start + 0.375, 0.1875),
        (42, start + 0.75, 0.1875),
        (42, start + 1.125, 0.1875),
        (36, start + 1.5, 0.375),  # Kick on beat 3
        (38, start + 1.875, 0.375), # Snare on beat 4
        (42, start + 1.5, 0.1875), # Hihat on 3 & 4
        (42, start + 1.6875, 0.1875),
        (42, start + 1.875, 0.1875),
        (42, start + 2.0625, 0.1875)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
