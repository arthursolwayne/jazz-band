
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
for bar in range(1):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375).add_to_track(drums)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125).add_to_track(drums)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75).add_to_track(drums)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5).add_to_track(drums)
    # Hihat
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125).add_to_track(drums)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, no repeating notes
bass_notes = [34, 35, 32, 31, 34, 35, 32, 31, 34, 35, 32, 31, 34, 35, 32, 31]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375).add_to_track(bass)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Cm7 = C, Eb, G, Bb
# F7 = F, A, C, Eb
chords = [
    # Bar 2
    (1.5 + 0.75, 'Fm7'),
    # Bar 3
    (1.5 + 2.25, 'Bb7'),
    # Bar 4
    (1.5 + 3.75, 'Cm7'),
]
for start, chord in chords:
    if chord == 'Fm7':
        pitches = [71, 67, 60, 58]
    elif chord == 'Bb7':
        pitches = [70, 65, 71, 67]
    elif chord == 'Cm7':
        pitches = [60, 58, 67, 65]
    for pitch in pitches:
        pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375).add_to_track(piano)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375).add_to_track(drums)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125).add_to_track(drums)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75).add_to_track(drums)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5).add_to_track(drums)
    # Hihat
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125).add_to_track(drums)

# Sax: Your motif
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Ab, Bb, C
sax_notes = [
    (1.5, 71),  # F
    (1.5 + 0.375, 67),  # Ab
    (1.5 + 0.75, 62),  # Bb
    (1.5 + 1.125, 60),  # C
    (1.5 + 1.5, 71),  # F (repeat)
    (1.5 + 1.875, 67),  # Ab
    (1.5 + 2.25, 62),  # Bb
    (1.5 + 2.625, 60),  # C
    (1.5 + 3.0, 71),  # F
    (1.5 + 3.375, 67),  # Ab
    (1.5 + 3.75, 62),  # Bb
    (1.5 + 4.125, 60)   # C
]
for start, pitch in sax_notes:
    pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375).add_to_track(sax)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
