
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick_times = [start + 0.0, start + 0.75]
    for t in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    snare_times = [start + 0.375, start + 1.125]
    for t in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Hi-hat on every eighth
    for i in range(8):
        t = start + i * 0.375
        note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Time signature: 4/4, tempo: 120 BPM

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 62, 100, 0.25),  # C
    (1.75, 63, 100, 0.25), # C#
    (2.0, 64, 100, 0.25),  # D
    (2.25, 62, 100, 0.25), # C
    # Bar 3
    (2.5, 60, 100, 0.25),  # Bb
    (2.75, 62, 100, 0.25), # C
    (3.0, 63, 100, 0.25),  # C#
    (3.25, 64, 100, 0.25), # D
    # Bar 4
    (3.5, 62, 100, 0.25),  # C
    (3.75, 63, 100, 0.25), # C#
    (4.0, 64, 100, 0.25),  # D
    (4.25, 62, 100, 0.25), # C
    (4.5, 60, 100, 0.25),  # Bb
    (4.75, 62, 100, 0.25), # C
    (5.0, 63, 100, 0.25),  # C#
    (5.25, 64, 100, 0.25), # D
]
for t, p, v, d in bass_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
# C7 on 2, F7 on 4
piano_notes = [
    (2.0, 60, 100, 0.25),  # C
    (2.0, 64, 100, 0.25),  # E
    (2.0, 67, 100, 0.25),  # G
    (2.0, 71, 100, 0.25),  # B
    (4.0, 65, 100, 0.25),  # F
    (4.0, 69, 100, 0.25),  # A
    (4.0, 71, 100, 0.25),  # B
    (4.0, 76, 100, 0.25),  # D
]
for t, p, v, d in piano_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    piano.notes.append(note)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * bar_length
    # Kick on 1 and 3
    kick_times = [start + 0.0, start + 0.75]
    for t in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    snare_times = [start + 0.375, start + 1.125]
    for t in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
        drums.notes.append(note)
    # Hi-hat on every eighth
    for i in range(8):
        t = start + i * 0.375
        note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
        drums.notes.append(note)

# Sax (Dante): One short motif, make it sing
# C -> E -> G -> C
sax_notes = [
    (1.5, 60, 100, 0.5),  # C
    (2.0, 64, 100, 0.5),  # E
    (2.5, 67, 100, 0.5),  # G
    (3.0, 60, 100, 0.5),  # C
]
for t, p, v, d in sax_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
