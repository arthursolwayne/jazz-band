
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    kick_time = i * 1.5 + 0.0
    snare_time = i * 1.5 + 0.75
    for j in range(2):
        hihat_time = i * 1.5 + j * 0.375
        hihat_note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(hihat_note)

    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(kick_note)

    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(snare_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, never the same note twice
# Fm7 = F, Ab, C, Eb
# Walking bass line: F, Gb, G, Ab, A, Bb, B, C, etc.

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=72, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=73, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=74, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=75, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=74, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=73, start=5.75, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db

# Bar 2: Fm7 on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.25),

    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),
]

# Bar 3: Bb7 on beat 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),

    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
])

# Bar 4: Eb7 on beat 2 and 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.5),

    pretty_midi.Note(velocity=90, pitch=59, start=6.0, end=6.25),
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.25),
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.25),
    pretty_midi.Note(velocity=90, pitch=66, start=6.0, end=6.25),
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, F
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=63, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
