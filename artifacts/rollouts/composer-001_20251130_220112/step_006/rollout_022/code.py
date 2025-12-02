
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
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length / 8))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + bar_length / 4),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.5 + bar_length / 4, end=1.5 + bar_length / 2),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=1.5 + bar_length / 2, end=1.5 + 3 * bar_length / 4),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=1.5 + 3 * bar_length / 4, end=1.5 + bar_length),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=1.5 + bar_length + bar_length / 4, end=1.5 + bar_length + bar_length / 2),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5 + bar_length + bar_length / 2, end=1.5 + bar_length + 3 * bar_length / 4),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.5 + bar_length + 3 * bar_length / 4, end=1.5 + 2 * bar_length),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=1.5 + 2 * bar_length, end=1.5 + 2 * bar_length + bar_length / 4),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=1.5 + 2 * bar_length + bar_length / 4, end=1.5 + 2 * bar_length + bar_length / 2),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=1.5 + 2 * bar_length + bar_length / 2, end=1.5 + 2 * bar_length + 3 * bar_length / 4),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=1.5 + 2 * bar_length + 3 * bar_length / 4, end=1.5 + 3 * bar_length),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + bar_length / 4),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + bar_length / 4),  # D7: A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + bar_length / 4),  # D7: F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + bar_length / 4),  # D7: C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + bar_length / 2, end=1.5 + bar_length / 2 + bar_length / 4),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + bar_length / 2, end=1.5 + bar_length / 2 + bar_length / 4),  # D7: A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + bar_length / 2, end=1.5 + bar_length / 2 + bar_length / 4),  # D7: F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + bar_length / 2, end=1.5 + bar_length / 2 + bar_length / 4),  # D7: C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4),  # D7: A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4),  # D7: F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4),  # D7: C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Melody: D, F, G, Eb (bar 2), D, F, G, Eb (bar 3), D, F, G, Eb (bar 4)
sax_notes = []
# Bar 2: D, F, G, Eb
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + bar_length / 4))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5 + bar_length / 4, end=1.5 + bar_length / 2))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5 + bar_length / 2, end=1.5 + 3 * bar_length / 4))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=61, start=1.5 + 3 * bar_length / 4, end=1.5 + bar_length))

# Bar 3: D, F, G, Eb
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5 + bar_length, end=1.5 + bar_length + bar_length / 4))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5 + bar_length + bar_length / 4, end=1.5 + bar_length + bar_length / 2))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5 + bar_length + bar_length / 2, end=1.5 + bar_length + 3 * bar_length / 4))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=61, start=1.5 + bar_length + 3 * bar_length / 4, end=1.5 + 2 * bar_length))

# Bar 4: D, F, G, Eb
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 2 * bar_length, end=1.5 + 2 * bar_length + bar_length / 4))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 2 * bar_length + bar_length / 4, end=1.5 + 2 * bar_length + bar_length / 2))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 2 * bar_length + bar_length / 2, end=1.5 + 2 * bar_length + 3 * bar_length / 4))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=61, start=1.5 + 2 * bar_length + 3 * bar_length / 4, end=1.5 + 3 * bar_length))
sax.notes.extend(sax_notes)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * bar_length + (beat * bar_length / 4)
        if beat % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length / 8))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
