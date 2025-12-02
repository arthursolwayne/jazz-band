
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drum_instrument = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drum_instrument)

bass_program = pretty_midi.instrument_name_to_program('Electric Bass (finger)')
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Tempo: 160 BPM
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Note: 160 BPM = 6 beats per 6 seconds (4 bars = 6 seconds). Each beat is 0.375 seconds.

# Bar 1: Drums only
# Little Ray's groove: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time per beat = 0.375s

def add_drums():
    bar_length = 4  # in beats
    for beat in range(bar_length):
        # Kick on 1 and 3
        if beat in [0, 2]:
            kick = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.1)
            drum_instrument.notes.append(kick)

        # Snare on 2 and 4
        if beat in [1, 3]:
            snare = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.1)
            drum_instrument.notes.append(snare)

        # Hi-hat on every eighth
        for i in range(2):  # two eighth notes per beat
            hihat = pretty_midi.Note(velocity=70, pitch=42, start=(beat * 0.375) + i * 0.1875,
                                     end=(beat * 0.375) + i * 0.1875 + 0.05)
            drum_instrument.notes.append(hihat)

# Bar 1: Drums only
add_drums()

# Bars 2–4: Full ensemble

# Define the time for each bar
bar1_time = 1.5  # 4 beats * 0.375s
bar2_time = bar1_time * 2
bar3_time = bar1_time * 3
bar4_time = bar1_time * 4

# Define the saxophone motif: simple, singable, with a "question" feel
# D, F#, A, B, D (scale: D major)
# Motif: D - F# - A - B - D (but with a suspension on the A, then resolve to D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar2_time, end=bar2_time + 0.2),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=bar2_time + 0.3, end=bar2_time + 0.5),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=bar2_time + 0.6, end=bar2_time + 0.8),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=bar2_time + 0.9, end=bar2_time + 1.1),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=bar3_time + 0.2, end=bar3_time + 0.6),  # D
]

for note in sax_notes:
    sax_instrument.notes.append(note)

# Bass line: walking line with chromatic approaches
def create_bass_line():
    # Dmaj7 = D F# A C#
    # Bass line: D - C# - F# - E - A - G - B - A
    # These are the notes (in MIDI pitch numbers)
    pitches = [62, 61, 67, 66, 69, 68, 71, 69]
    velocities = [100] * len(pitches)
    for i, pitch in enumerate(pitches):
        start = bar2_time + i * 0.375
        end = start + 0.375
        bass_note = pretty_midi.Note(velocity=velocities[i], pitch=pitch, start=start, end=end)
        bass_instrument.notes.append(bass_note)

create_bass_line()

# Piano: 7th chords on 2 and 4
def create_piano_line():
    # D7 = D F# A C
    # G7 = G B D F
    # C7 = C E G B
    # F7 = F A C E
    chords = [
        [62, 67, 69, 64],  # D7
        [71, 76, 62, 67],  # G7
        [60, 64, 67, 71],  # C7
        [65, 69, 62, 67],  # F7
    ]
    for bar in range(2, 5):
        time = bar * bar1_time
        for i, chord in enumerate(chords):
            if i % 2 == 1:  # Comp on 2 and 4 (i=1,3)
                for note in chord:
                    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
                    piano_instrument.notes.append(piano_note)

create_piano_line()

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file saved as 'jazz_intro.mid'")
