
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
for bar in range(1):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Fm b9
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Fm 7
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),  # Fm b7
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Fm 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75), # Fm b7
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Fm 9
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # Fm root
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # Fm b9
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25), # Fm 7
    pretty_midi.Note(velocity=100, pitch=37, start=5.25, end=5.625), # Fm b7
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Fm 3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Db
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875), # Db
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5 - 2.25s): first phrase
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 3 (2.25 - 3.0s): rest
# No sax here, let it hang

# Bar 4 (3.0 - 3.75s): second phrase, finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # Eb
]
sax.notes.extend(sax_notes)

# Bar 4 (3.75 - 4.5s): continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 5.25s): resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4 (5.25 - 6.0s): final resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    time = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
