
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
bar1_start = 0.0
bar1_end = 1.5
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
hihat_times = [bar1_start + x * 0.375 for x in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), E (chromatic approach), C (fifth), D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=71, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=70, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=76, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=77, start=bar2_start + 1.125, end=bar2_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=74, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=79, start=bar2_start, end=bar2_start + 0.375),
    
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=72, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 1.5, end=bar2_start + 1.875),
    
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=100, pitch=79, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=100, pitch=81, start=bar2_start + 3.0, end=bar2_start + 3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 3.0, end=bar2_start + 3.375)
]
piano.notes.extend(piano_notes)

# Drums: Same pattern as bar 1
kick_times = [bar2_start + 0.375, bar2_start + 1.125]
snare_times = [bar2_start + 0.75, bar2_start + 1.5]
hihat_times = [bar2_start + x * 0.375 for x in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Sax: Motif in F (F, G, Bb, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=72, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=74, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=71, start=bar2_start + 1.125, end=bar2_start + 1.5),
    
    # Rest of the motif in bar 3, leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=110, pitch=72, start=bar2_start + 1.875, end=bar2_start + 2.25),
    pretty_midi.Note(velocity=110, pitch=74, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=110, pitch=71, start=bar2_start + 2.625, end=bar2_start + 3.0)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Bass: Walking line in Gm7 (G, Bb, D, F)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=71, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=76, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=77, start=bar3_start + 1.125, end=bar3_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings (same as bar 2)
piano_notes = [
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=72, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=76, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 0.375),
    
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=81, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 1.5, end=bar3_start + 1.875)
]
piano.notes.extend(piano_notes)

# Drums: Same pattern as bar 1
kick_times = [bar3_start + 0.375, bar3_start + 1.125]
snare_times = [bar3_start + 0.75, bar3_start + 1.5]
hihat_times = [bar3_start + x * 0.375 for x in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Bass: Walking line in C7 (C, E, G, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=79, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=81, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=71, start=bar4_start + 1.125, end=bar4_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings (same as bar 2)
piano_notes = [
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=79, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=81, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start, end=bar4_start + 0.375)
]
piano.notes.extend(piano_notes)

# Drums: Same pattern as bar 1
kick_times = [bar4_start + 0.375, bar4_start + 1.125]
snare_times = [bar4_start + 0.75, bar4_start + 1.5]
hihat_times = [bar4_start + x * 0.375 for x in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Sax: Finishing the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=72, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=74, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=71, start=bar4_start + 1.125, end=bar4_start + 1.5)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
