
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Time in seconds per bar (160 BPM, 4/4)
time_per_bar = 1.5  # 60 / 160 * 4 = 1.5

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, kick),
    (0.375, hihat),
    (0.75, kick),
    (1.125, hihat),
    (1.5, snare),
    (1.875, hihat),
    (2.25, kick),
    (2.625, hihat),
    (3.0, snare),
    (3.375, hihat)
]

for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# BAR 2: Full quartet (1.5 - 3.0s)

# Bass line: Marcus on walking line, chromatic approaches
# Fm7: F, Ab, Bb, D
# Walking line in Fm: F, Gb, G, Ab, A, Bb, B, C, etc.
# Bar 2: F, Gb, G, Ab (each on beat)

bass_notes = [
    (1.5, 64),  # F
    (1.875, 65),  # Gb
    (2.25, 66),  # G
    (2.625, 67),  # Ab
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(bass_note)

# Piano: Diane on 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, D
# Bar 2: Root on beat 1, 7th on beat 3 (comp on 2 and 4)
piano_notes = [
    (1.5, 64),  # F
    (1.875, 67),  # Ab (comp)
    (2.25, 69),  # Bb
    (2.625, 71),  # D (comp)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(piano_note)

# Sax: Dante's motif — a short, singable phrase that lingers
# Fm: F, Ab, Bb, C, D, Eb, G, A
# Motif: F → Ab → Bb → C (rising minor third to major second with a hint of dissonance)
# Start on beat 1, end on beat 3, leave it hanging on beat 4

sax_notes = [
    (1.5, 64),  # F
    (1.875, 67),  # Ab
    (2.25, 69),  # Bb
    (2.625, 71),  # C
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.2)
    sax.notes.append(sax_note)

# BAR 3: Full quartet (3.0 - 4.5s)

# Bass: Continue walking line
bass_notes = [
    (3.0, 72),  # A
    (3.375, 73),  # Bb
    (3.75, 74),  # B
    (4.125, 76),  # C
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(bass_note)

# Piano: Fm7 again, comp on 2 and 4
piano_notes = [
    (3.0, 64),  # F
    (3.375, 67),  # Ab (comp)
    (3.75, 69),  # Bb
    (4.125, 71),  # D (comp)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(piano_note)

# Sax: Repeat the motif with slight variation (Ab instead of F on beat 1)
sax_notes = [
    (3.0, 67),  # Ab
    (3.375, 69),  # Bb
    (3.75, 71),  # C
    (4.125, 73),  # D (hang)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.2)
    sax.notes.append(sax_note)

# BAR 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line continues
bass_notes = [
    (4.5, 76),  # C
    (4.875, 77),  # C#
    (5.25, 78),  # D
    (5.625, 80),  # Eb
]
for time, note in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(bass_note)

# Piano: Fm7 again, comp on 2 and 4
piano_notes = [
    (4.5, 64),  # F
    (4.875, 67),  # Ab (comp)
    (5.25, 69),  # Bb
    (5.625, 71),  # D (comp)
]
for time, note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(piano_note)

# Sax: End the motif with a resolution or question
# Fm: F → Ab → Bb → C → D (maybe) with a little chromatic pull
sax_notes = [
    (4.5, 64),  # F (resolve or restate)
    (4.875, 67),  # Ab
    (5.25, 69),  # Bb
    (5.625, 73),  # D (hang)
]
for time, note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.2)
    sax.notes.append(sax_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
