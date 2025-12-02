
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Fill the bar with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
for tick in [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0]:
    if tick % 1.5 == 0.0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    if tick % 1.5 == 0.75:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=38, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    # Hi-hats on every eighth
    note = pretty_midi.Note(velocity=80, pitch=42, start=tick, end=tick + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43)
# Root, chromatic approach, fifth, root
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=39, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=43, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=bar2_start + 1.125, end=bar2_start + 1.5)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar
# Bar 2: D7 (D-F#-A-C#)
note_d = pretty_midi.Note(velocity=90, pitch=62, start=bar2_start, end=bar2_end)
note_fsharp = pretty_midi.Note(velocity=80, pitch=67, start=bar2_start, end=bar2_end)
note_a = pretty_midi.Note(velocity=90, pitch=69, start=bar2_start, end=bar2_end)
note_csharp = pretty_midi.Note(velocity=80, pitch=71, start=bar2_start, end=bar2_end)
piano.notes.extend([note_d, note_fsharp, note_a, note_csharp])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for tick in [bar2_start, bar2_start + 0.75, bar2_start + 1.5, bar2_start + 2.25, bar2_start + 3.0, bar2_start + 3.75, bar2_start + 4.5, bar2_start + 5.25, bar2_start + 6.0]:
    if tick % 1.5 == 0.0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    if tick % 1.5 == 0.75:
        note = pretty_midi.Note(velocity=110, pitch=38, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=tick, end=tick + 0.125)
    drums.notes.append(note)

# Dante: Tenor sax motif
# Start with a short phrase that sings, leave it hanging
dante_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start, end=bar2_start + 0.25),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.25, end=bar2_start + 0.5),  # F#5
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.5, end=bar2_start + 0.75),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 1.0, end=bar2_start + 1.25),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 1.25, end=bar2_start + 1.5)  # F#5
]
sax.notes.extend(dante_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Marcus: Walking line again, but with a chromatic approach to G
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=44, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=47, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=43, start=bar3_start + 1.125, end=bar3_start + 1.5)
]
bass.notes.extend(bass_notes)

# Diane: Dm7 (D-F-A-C)
note_d = pretty_midi.Note(velocity=90, pitch=62, start=bar3_start, end=bar3_end)
note_f = pretty_midi.Note(velocity=80, pitch=67, start=bar3_start, end=bar3_end)
note_a = pretty_midi.Note(velocity=90, pitch=69, start=bar3_start, end=bar3_end)
note_c = pretty_midi.Note(velocity=80, pitch=72, start=bar3_start, end=bar3_end)
piano.notes.extend([note_d, note_f, note_a, note_c])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for tick in [bar3_start, bar3_start + 0.75, bar3_start + 1.5, bar3_start + 2.25, bar3_start + 3.0, bar3_start + 3.75, bar3_start + 4.5, bar3_start + 5.25, bar3_start + 6.0]:
    if tick % 1.5 == 0.0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    if tick % 1.5 == 0.75:
        note = pretty_midi.Note(velocity=110, pitch=38, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=tick, end=tick + 0.125)
    drums.notes.append(note)

# Dante: Continue the motif, but with a twist
dante_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar3_start, end=bar3_start + 0.25),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + 0.25, end=bar3_start + 0.5),  # E5
    pretty_midi.Note(velocity=100, pitch=62, start=bar3_start + 0.5, end=bar3_start + 0.75),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + 0.75, end=bar3_start + 1.0),  # E5
    pretty_midi.Note(velocity=100, pitch=62, start=bar3_start + 1.0, end=bar3_start + 1.25),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + 1.25, end=bar3_start + 1.5)  # E5
]
sax.notes.extend(dante_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Marcus: Walking line again, resolve on G
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=49, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=47, start=bar4_start + 1.125, end=bar4_start + 1.5)
]
bass.notes.extend(bass_notes)

# Diane: G7 (G-B-D-F#)
note_g = pretty_midi.Note(velocity=90, pitch=67, start=bar4_start, end=bar4_end)
note_b = pretty_midi.Note(velocity=80, pitch=71, start=bar4_start, end=bar4_end)
note_d = pretty_midi.Note(velocity=90, pitch=69, start=bar4_start, end=bar4_end)
note_fsharp = pretty_midi.Note(velocity=80, pitch=74, start=bar4_start, end=bar4_end)
piano.notes.extend([note_g, note_b, note_d, note_fsharp])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for tick in [bar4_start, bar4_start + 0.75, bar4_start + 1.5, bar4_start + 2.25, bar4_start + 3.0, bar4_start + 3.75, bar4_start + 4.5, bar4_start + 5.25, bar4_start + 6.0]:
    if tick % 1.5 == 0.0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    if tick % 1.5 == 0.75:
        note = pretty_midi.Note(velocity=110, pitch=38, start=tick, end=tick + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=tick, end=tick + 0.125)
    drums.notes.append(note)

# Dante: Finish the motif with a resolution
dante_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start, end=bar4_start + 0.25),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 0.25, end=bar4_start + 0.5),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 0.5, end=bar4_start + 0.75),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 0.75, end=bar4_start + 1.0),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 1.0, end=bar4_start + 1.25),  # F#5
    pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 1.25, end=bar4_start + 1.5)  # G5
]
sax.notes.extend(dante_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
