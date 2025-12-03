
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus (bass): walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # C (E2)
    pretty_midi.Note(velocity=90, pitch=75, start=2.25, end=2.625),  # Bb (D#2)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # F (D2)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=3.0),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # G (F)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus (bass): walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # C (E2)
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),  # Bb (D#2)
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # F (D2)
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # C (E2)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus (bass): walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # F (D2)
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # C (E2)
    pretty_midi.Note(velocity=90, pitch=75, start=5.25, end=5.625),  # Bb (D#2)
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # F (D2)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # G (F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_start = bar_start + 0.0
    snare_start = bar_start + 0.75
    hihat_start = bar_start + 0.0
    kick_end = kick_start + 0.375
    snare_end = snare_start + 0.375
    hihat_end = hihat_start + 0.1875

    # Kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat
    for i in range(0, 8):
        hihat_time = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
